<template>
  <div>
    <component v-bind:is="components[selected.value]" :selected_file="selected_file" @exportFile="exportFile"></component>
  </div>
</template>

<script>
import Upload from './../views/Upload';
import Statistics from './../views/Statistics';

export default {
  name: "Body",
  props: ["selected"],
  components: {
    Upload,
    Statistics,
  },
  data(){
    return({
      components: {
        "upload": Upload,
        "stats": Statistics
      },
      selected_file: ""
    })
  },
  watch: {
    selected: {
      immediate: true,
      handler() {
        
      }
    }
  },
  methods: {
    exportFile(file){
      this.selected_file = file;
    }
  }
};
</script>

<style>
</style>