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
    <loading :active.sync="isLoading" :can-cancel="true" :is-full-page="false" :opacity="0.2"></loading>
  </div>
</template>

<script>
import axios from 'axios';
import vSelect from "vue-select";
import "vue-select/dist/vue-select.css";
import Loading from "vue-loading-overlay";



export default {
  components: {
    vSelect,
    Loading
  },
  created(){
    this.get_files();
  },
  data(){
    return {
      fileSelected: "",
      files: [],
      isLoading: false
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
      this.isLoading = true;

      axios 
      .post("http://localhost:5001/waveform?filename="+ this.fileSelected)
      .then(response => {
      })
      .catch(error => {});
      axios 
      .post("http://localhost:5001/analyze?filename="+ this.fileSelected)
      .then(response => {
      })
      .catch(error => {});
      axios 
      .post("http://localhost:5001/transcribe?filename="+ this.fileSelected)
      .then(response => {
        this.$emit('exportFile', this.fileSelected);
        this.isLoading = false;
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