<template>
  <div class="render">
    <svg id="svg-container" viewBox="-430 -100 2000 900" xmlns="http://www.w3.org/2000/svg">
<!--      <text  x="0" v-bind:y="get_y()">бля</text>&lt;!&ndash;v-for="n in 3" v-text="n"&ndash;&gt;-->
<!--      <text x="40" y="55">cat</text>-->
    </svg>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "AsciiRender",
  data(){
    return{
      ascii_array: [],

    }
  },
  methods: {
    async get_ascii(){
      await axios
      .get('api/v1/get_ascii')
      .then(response => {

        this.ascii_array = response.data.res
        console.log(this.ascii_array)
        this.fill_svg()

      })
      .catch(error => {
        console.log('Ошибка при загрузке ascii-фреймов')
      })
    },


    fill_svg(){
      let frames = this.ascii_array

      async function renderElementsWithDelay() {
        for (const frame of frames) {
          let text_attrs = ''
          let i = 0

          frame.forEach(function (row){
            text_attrs = text_attrs + `<text x="0" y="${i}" style="font-size: 10.5202px; font-family: monospace; dominant-baseline: hanging; white-space: pre;">${row}</text>`
            i += 13
          })

          document.getElementById("svg-container").innerHTML = text_attrs
          await new Promise(resolve => setTimeout(resolve, 44));
        }
        renderElementsWithDelay();
      }
      renderElementsWithDelay();
    },
  },
  mounted() {
    this.get_ascii()
  }
}
</script>

<style>

text {
   fill: white;
}

#svg-container {
  /*position: relative;*/
  /*left: 20%;*/
}

</style>