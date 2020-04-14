<template>
  <div>
    Please select a Audio file.
    <vSelect :options="files" v-model="fileSelected" label="name" ></vSelect>
    <button @click="transcribe">Transcribe</button>
  </div>
</template>

<script>
import axios from 'axios';
import vSelect from "vue-select";
import "vue-select/dist/vue-select.css";


export default {
  components: {
    vSelect
  },
  created(){
    this.get_files();
  },
  data(){
    return {
      fileSelected: "",
      files: []
    }
  },
  watch: {
    fileSelected: {
      handler(){
        this.$emit('exportFile', this.fileSelected);
      }
    }
  },
  methods: {
    get_files(){
      axios 
      .get("http://localhost:5001/listAudioFiles?foldername=input")
      .then(response => {
        this.files = response["data"];
      })
      .catch(error => {});
    },
    transcribe(){
      axios 
      .post("http://localhost:5001/waveform?filename=input/"+ this.fileSelected)
      .then(response => {
      })
      .catch(error => {});
      
    }
  }
}
</script>

<style>

</style>