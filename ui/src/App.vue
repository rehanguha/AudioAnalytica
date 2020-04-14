<template>
  <div id="app">
    <SideNav @selectedTab="selectedTab"></SideNav>
    <Body :selected="selected"></Body>
    <!-- <HelloWorld msg="Welcome to Your Vue.js App" /> -->
  </div>
</template>

<script>
import SideNav from "./components/SideNav";
import Body from "./components/Body";
import Upload from "./views/Upload";

import _ from "lodash";
export default {
  name: "App",
  components: {
    SideNav,
    Body
  },
  data() {
    return {
      selected: {value: "upload"}
    };
  },
  methods: {
    selectedTab: function(selected){
      this.selected = selected;
    }
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  display: grid;
  grid-template-columns: 300px auto;
}
</style>
