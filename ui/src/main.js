import Vue from "vue";
import App from "./App.vue";
import Highcharts from "highcharts";
import HighchartsVue from "highcharts-vue";
Vue.use(HighchartsVue, { Highcharts });
Vue.config.productionTip = false;

new Vue({
  render: h => h(App)
}).$mount("#app");
