const WebpackNotifierPlugin = require('webpack-notifier');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const { resolve } = require('path');

module.exports = {
    entry: ['babel-polyfill', './src/app/index.jsx'],
    output: {
        filename: '[name].js',
        path: resolve(__dirname, './build/app')
    },
    devtool: 'eval-source-map',
    devServer: {
        inline: true,
        historyApiFallback: true,
        proxy: {
            '/api': {
                target: 'http://localhost:3000',
                pathRewrite: {'^/api' : ''}
            }
        }
    },
    module: {
        rules: [
            {
                test: /\.jsx?$/,
                exclude: /node_modules/,
                use: {
                    loader: 'babel-loader',
                    options: {
                        presets: ['env', 'react']
                    }
                }
            }
        ]
    },
    resolve: {
        extensions: ['.js', '.jsx']
    },
    plugins: [
        new WebpackNotifierPlugin({
            alwaysNotify: true
        }),
        new HtmlWebpackPlugin({
            template: 'src/app/index.html'
        })
    ]
};
