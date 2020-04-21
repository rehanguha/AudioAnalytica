<template>
  <div>
    <h1>AudioAnalytica</h1>
    <p>description about audio analytica</p>
    <p>Please select a Audio file.</p>
    <div>
      <vSelect :options="files" v-model="fileSelected" label="name" ></vSelect>
    </div>
    <div>
      <button @click="transcribe" class="upload btn btn-primary">Upload</button>
    </div>
    
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
      .post("http://localhost:5001/waveform?filename="+ this.fileSelected)
      .then(response => {
        this.$emit('exportFile', this.fileSelected);
      })
      .catch(error => {});
      axios 
      .post("http://localhost:5001/analyze?filename="+ this.fileSelected)
      .then(response => {
        this.$emit('exportFile', this.fileSelected);
      })
      .catch(error => {});      
    }
  }
}
</script>

<style>
  .upload{
    margin-top:20px;
  }
  .v-select {
    width: 50%;
    display: inline-block;
  }
</style>