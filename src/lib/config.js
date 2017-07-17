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
            channels: {
                1: 100,
                2: 104,
                3: 200,
                4: 204,
                5: 300,
                6: 304
            },
            links: {
                12: 0,
                34: 2,
                56: 3
            },
            recording: 1
        },
        recordBtn: 17,
        mcps: [ // TODO: Add real mcp addresses
            {
                offset: 100,
                address: 32
            },
            {
                offset: 200,
                address: 64
            },
            {
                offset: 300,
                address: 96
            }
        ]
    }
};
