<template>
  <div>
    <h4>Waveplot</h4>
    <img v-bind:src="wave_image">
    <h4>Spec</h4>
    <img :src="spec_image">
  </div>

</template>

<script>

import axios from 'axios';

export default {
  props: ["selectedFile"],
  data(){
    return {
      wave_image: "",
      spec_image: ""
    }
  },
  mounted(){
    this.get_waveform_images();
  },
  methods: {
    get_waveform_images(){
      axios
        .get("http://localhost:5001/wave_image?filename=" + this.selectedFile, { responseType: "blob" })
        .then(response => {
          this.wave_image = URL.createObjectURL(response.data);
        })
        .catch(error => {});      
      axios
        .get("http://localhost:5001/spec_image?filename=" + this.selectedFile, { responseType: "blob" })
        .then(response => {
          this.spec_image = URL.createObjectURL(response.data);
        })
        .catch(error => {});      

    }
  }
}
</script>

<style>

</style>