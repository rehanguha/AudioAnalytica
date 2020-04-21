<template>
  <div>
    <h2>Channel Comparison</h2>
    <p>description</p>
    <div class="json-compare">
      <div>
        <json-viewer :value="channel1" boxed :expand-depth=1 copyable ></json-viewer>
      </div>
      <div>
        <json-viewer :value="channel2" boxed :expand-depth=1 copyable></json-viewer>
      </div>
    </div>    
  </div>
</template>

<script>
import JsonViewer from 'vue-json-viewer';
import axios from 'axios';
export default {
  props: ["selectedFile"],
  components: {
    JsonViewer
  },
  mounted(){
    this.get_channel_data();
  },
  data() {
    return {
      channel1: {},
      channel2: {}
    }
  },
  methods: {
    get_channel_data: function(){
          axios
      .get("http://localhost:5001/fe?filename=" + this.selectedFile)
      .then(response => {
        this.channel1 = response["data"]["channel1"];
        this.channel2 = response["data"]["channel2"];
      })
      .catch(error => {});
    }
  }
}
</script>

<style >
  .json-compare{
    display: grid;
    grid-template-columns: 50% 50%;    
  }
  .json-tree-root{
    min-width: 0px !important;
  }
  .jv-container .jv-code.boxed {
    max-height: 500px;
    overflow: auto;
  }
</style>