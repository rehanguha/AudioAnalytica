/* eslint-disable no-debugger */
<template>
<div>
  <sidebar-menu :menu="menu" :width="'300px'" :hideToggle="true" @item-click="onItemClick" />
</div>
</template>

<script>
import { SidebarMenu } from "vue-sidebar-menu";
import "vue-sidebar-menu/dist/vue-sidebar-menu.css";
import Upload from "./../views/Upload";
import Statistics from "./../views/Statistics";
import _ from "lodash";
export default {
  name: "SideNav",
  props: ["selected"],
  components: {
    SidebarMenu
  },
  methods: {
    onItemClick: function(event, item) {
      var temp = _.cloneDeep(this.menu);
      _.each(temp, e => (e.class = ""));
      var selected = _.first(_.filter(temp, e => e.value == item.value));
      selected.class = "vsm--link_active vsm--link_exact-active";
      this.menu = temp;
      this.$emit("selectedTab", selected);
    },
  },
  data() {
    return ({
      menu: [
        {
          header: true,
          title: "AudioAnalytica",
          value: "title",
          hiddenOnCollapse: true
        },
        {
          title: "Upload Audio",
          value: "upload",
          icon: "fa fa-user",
          class: "vsm--link_active vsm--link_exact-active"
        },
        {
          title: "Statistics",
          value: "stats",
          icon: "fa fa-chart-area",
          class: ""
        },
        {
          title: "Analytics",
          value: "analytics",
          icon: "fa fa-chart-area"
        },
        {
          title: "Transcribtion",
          value: "transcribtion",
          icon: "fa fa-chart-area"
        },
        {
          title: "Share",
          value: "share",
          icon: "fa fa-chart-area"
        }
      ]
    });
  }
};
</script>
<style>
.v-sidebar-menu .vsm--header {
  text-transform: unset;
}
.v-sidebar-menu .vsm_expanded {
  max-width: 300px;
}
</style>