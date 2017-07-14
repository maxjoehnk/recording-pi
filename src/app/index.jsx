import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import MainFrame from './components/main/MainFrame';
import { MuiThemeProvider } from 'material-ui/styles';

import store from './store/index.js';

ReactDOM.render(
    <Provider store={store}>
        <MuiThemeProvider>
            <MainFrame/>
        </MuiThemeProvider>
    </Provider>,
    document.getElementById('app')
);
