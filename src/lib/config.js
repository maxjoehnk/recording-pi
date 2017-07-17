module.exports = {
    sessionPath: '/Users/max/Documents/Code/recording-pi/sessions', // Dev Path
    ports: {
        clientApi: 3000,
        hostApi: 4000,
        python: 5000
    },
    gpio: {
        // Free Ports: 6, 7
        // Ports 8-16 are special function ports
        // Ports 4-5 are used for the Display
        // Ports 18-20 are used for the Encoder
        leds: {
            channels: [
                {
                    channel: 1,
                    base: 100
                },
                {
                    channel: 2,
                    base: 104
                },
                {
                    channel: 3,
                    base: 200
                },
                {
                    channel: 4,
                    base: 204
                },
                {
                    channel: 5,
                    base: 300
                },
                {
                    channel: 6,
                    base: 304
                }
            ],
            links: [
                {
                    channels: 12,
                    port: 0
                },
                {
                    channels: 34,
                    port: 2
                },
                {
                    channels: 56,
                    port: 3
                }
            ],
            recording: 1
        },
        recordBtn: 17,
        mcps: [
            {
                offset: 100,
                address: 32
            },
            {
                offset: 200,
                address: 36
            },
            {
                offset: 300,
                address: 38
            }
        ]
    },
    threshold: [
        0.1,
        0.3,
        0.6,
        1
    ]
};
