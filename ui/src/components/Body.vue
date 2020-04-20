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
  props: ["selected", "sendFile"],
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
    selected_file: {
      immediate: true,
      handler() {
        this.$emit('sendFile',this.selected_file);
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