#include <gst/gst.h>
#include "recorder.h"
#include <string>
#include <sstream>

#include <iostream>
#include <math.h>

bool recording = false;
GstElement *pipeline;
GstElement *audioinput, *audioconvert, *level, *fakesink, *fileencode, *fileoutput, *tee, *queue1, *queue2;
GstBus *bus;
guint watch_id;
GMainLoop *loop;

// @TODO: Refactor
static gboolean
message_handler (GstBus * bus, GstMessage * message, gpointer data)
{

  if (message->type == GST_MESSAGE_ELEMENT) {
    const GstStructure *s = gst_message_get_structure (message);
    const gchar *name = gst_structure_get_name (s);

    if (strcmp (name, "level") == 0) {
      gint channels;
      gdouble rms_dB;
      gdouble rms;
      const GValue *array_val;
      const GValue *value;
      GValueArray *rms_arr;
      gint i;

      /* the values are packed into GValueArrays with the value per channel */
      array_val = gst_structure_get_value (s, "rms");
      rms_arr = (GValueArray *) g_value_get_boxed (array_val);

      /* we can get the number of channels as the length of any of the value
       * arrays */
      channels = rms_arr->n_values;
      for (i = 0; i < channels; ++i) {

        value = g_value_array_get_nth (rms_arr, i);
        rms_dB = g_value_get_double (value);

        /* converting from dB to normal gives us a value between 0.0 and 1.0 */
        rms = pow (10, rms_dB / 20);

        std::cout << "rms " << rms << " on channel " << i << std::endl;
        //visualize_rms(i, rms);
      }
    }
  }
  /* we handled the message we want, and ignored the ones we didn't want.
   * so the core can unref the message for us */
  return TRUE;
}

int init_recorder() {
    pipeline = gst_pipeline_new(NULL);
    g_assert(pipeline);
    audioinput = gst_element_factory_make("autoaudiosrc", NULL);
    g_assert(audioinput);
    tee = gst_element_factory_make("tee", NULL);
    g_assert(tee);
    queue1 = gst_element_factory_make("queue", NULL);
    g_assert(queue1);
    audioconvert = gst_element_factory_make("audioconvert", NULL);
    g_assert(audioconvert);
    level = gst_element_factory_make("level", NULL);
    g_assert(level);
    fakesink = gst_element_factory_make("fakesink", NULL);
    g_assert(fakesink);

    gst_bin_add_many(GST_BIN (pipeline), audioinput, tee, queue1, audioconvert, level, fakesink, NULL);

    if (!gst_element_link(audioinput, tee)) {
        g_error("Failed to link audioinput and tee");
    }
    if (!gst_element_link(tee, queue1)) {
        g_error("Failed to link tee and queue1");
    }
    if (!gst_element_link(queue1, audioconvert)) {
        g_error("Failed to link queue1 and audioconvert");
    }
    if (!gst_element_link(audioconvert, level)) {
        g_error("Failed to link audioconvert and level");
    }
    if (!gst_element_link(level, fakesink)) {
        g_error("Failed to link level and fakesink");
    }

    g_object_set(G_OBJECT (level), "post-messages", true, NULL);
    g_object_set(G_OBJECT (fakesink), "sync", true, NULL);

    gst_element_set_state (pipeline, GST_STATE_PLAYING);

    bus = gst_element_get_bus(pipeline);
    watch_id = gst_bus_add_watch(bus, message_handler, NULL);

    //loop = g_main_loop_new(NULL, false);
    //g_main_loop_run(loop);
    return 0;
}

void main_loop() {
    GstMessage *msg;
    while (1) {
        while ((msg = gst_bus_pop (bus))) {
          // Call your bus message handler
          message_handler (bus, msg, NULL);
          gst_message_unref (msg);
        }
    }
}

void terminate_recorder() {
    g_source_remove(watch_id);
    //g_main_loop_unref(loop);
}

void start_recording(std::string path, std::string prefix) {
    std::cout << "Starting recording" << std::endl;
    queue2 = gst_element_factory_make("queue", NULL);
    g_assert(queue2);
    fileencode = gst_element_factory_make("wavenc", NULL);
    g_assert(fileencode);
    fileoutput = gst_element_factory_make("filesink", NULL);
    g_assert(fileoutput);

    gst_bin_add_many(GST_BIN(pipeline), queue2, fileencode, fileoutput, NULL);

    if (!gst_element_link(tee, queue2)) {
        g_error("Failed to link tee and queue2");
    }
    if (!gst_element_link_filtered(queue2, fileencode, NULL)) {
        g_error("Failed to link queue2 and fileencode");
    }
    if (!gst_element_link(fileencode, fileoutput)) {
        g_error("Failed to link fileencode and fileoutput");
    }

    std::ostringstream filename;
    filename << path << "/" << prefix << ".wav";
    g_object_set(G_OBJECT(fileoutput), "location", filename.str().c_str());

    std::cout << "Started recording" << std::endl;
}

void stop_recording() {
    gst_element_unlink(tee, queue2);
    gst_element_unlink(queue2, fileencode);
    gst_element_unlink(fileencode, fileoutput);
}

bool is_recording() {
    return recording;
}
