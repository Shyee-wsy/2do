import Vue from 'vue'
import App from './App.vue'
import {server} from "./providers/apis"
Vue.prototype.$server = server;
new Vue({
  el: '#app',
  render: h => h(App)
})
