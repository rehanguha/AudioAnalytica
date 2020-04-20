<template>
  <div class="json-compare">
    <div>
      <vue-json-tree :raw="JSON.stringify(channel1)" ></vue-json-tree>
    </div>
    <div>
      <vue-json-tree :raw="JSON.stringify(channel2)" ></vue-json-tree>
    </div>
  </div>

</template>

<script>
import VueJsonTree from 'vue-json-tree';
import axios from 'axios';
export default {
  props: ["selectedFile"],
  components: {
    VueJsonTree
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
</style>