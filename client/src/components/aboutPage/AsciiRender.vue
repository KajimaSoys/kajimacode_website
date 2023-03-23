<template>
  <div class="loading" @click="stopAnimation" ref="loading">
    <div class="render" ref="render">
      <svg id="svg-container" viewBox="0 0 1850 1300" xmlns="http://www.w3.org/2000/svg">
      </svg>
    </div>

    <div class="stop" ref="stop">
      {{ this.$store.state.language.language === 'ru' ? 'Пропустить..' : 'Click to continue..'}}
    </div>

    <div class="backdown" ref="backdown">
      <div class="left" ref="left"> </div>
      <div class="right" ref="right"> </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "AsciiRender",
  data(){
    return{
      ascii_array: [],
      num_files: 15,
    }
  },
  methods: {
    async get_ascii(index){
      try {
        if (index <= this.num_files) {
          const response = await axios.get(`api/v1/get_ascii_part_${index}`);
          const ascii_array = response.data.res;
          this.build_text_attrs(ascii_array);
          this.get_ascii(index + 1);
        } else {
          this.stopAnimation();
        }
      } catch (error) {
        console.log('Error');
      }
    },

    async build_text_attrs(ascii_array){
      for (const frame of ascii_array) {
        let text_attrs = '';
        let i = 0;
        for (const row of frame) {
          text_attrs += `<text x="0" y="${i}" style="font-size: 10.5202px; font-family: monospace; dominant-baseline: hanging; white-space: pre; fill: white;">${row}</text>`;
          i += 13;
        }
        document.getElementById('svg-container').innerHTML = text_attrs;
        await new Promise(resolve => setTimeout(resolve, 30));
      }
    },

    // fill_svg(){
    //   let frames = this.ascii_array
    //
    //   async function renderElementsWithDelay() {
    //     console.log('render started')
    //     for (const frame of frames) {
    //       let text_attrs = ''
    //       let i = 0
    //
    //       frame.forEach(function (row){
    //         text_attrs = text_attrs + `<text x="0" y="${i}" style="font-size: 10.5202px; font-family: monospace; dominant-baseline: hanging; white-space: pre; fill: white;">${row}</text>`
    //         i += 13
    //       })
    //
    //       document.getElementById("svg-container").innerHTML = text_attrs
    //       await new Promise(resolve => setTimeout(resolve, 30));
    //     }
    //     // renderElementsWithDelay();
    //     // console.log('render finished')
    //
    //   }
    //
    //   window.scrollTo({top:0,behavior:'auto'});
    //   renderElementsWithDelay().then(() => {
    //     this.stopAnimation()
    //   })
    //
    // },

    stopAnimation(){
      // console.log('stop animation')

        this.$refs.render.style.opacity = '0'
        this.$refs.stop.style.opacity = '0'

      setTimeout(() => {
        this.$refs.render.style.display = 'none'
        this.$refs.stop.style.display = 'none'
        this.$refs.loading.style.height = '0'
      },300)

      setTimeout(() => {
        this.$refs.left.style.transform = 'translateX(-100%)'
        this.$refs.right.style.transform = 'translateX(100%)'
      }, 300)

      setTimeout(() => {
        this.$refs.backdown.style.display = 'none'
        document.body.style.overflow = 'auto'

      }, 1000)
      //
    }
  },
  created() {
    document.body.style.overflow = 'hidden'
    window.scrollTo({top:0,behavior:'auto'});
    this.get_ascii(1)
  },
}
</script>

<style scoped>

.loading {
  background-color: #1d2939;
  position: relative;
  z-index: 1001;
  cursor: pointer;
  height: 100vh;
}

.render {
  max-width: 55%;
  margin-left: auto;
  margin-right: auto;
  transition: opacity 0.3s ease-in-out;
}

.stop {
  color: white;
  text-align: center;
  font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Fira Sans', 'Droid Sans', 'Helvetica Neue', sans-serif;
  font-size: 1rem;
  line-height: 1.5;
  letter-spacing: normal;
  transition: opacity 0.3s ease-in-out, color 0.2s ease-in-out;
  position: fixed;
  width: 100%;
  margin-left: auto;
  margin-right: auto;
  z-index: 1;
  bottom: 60px;
}

.stop:hover {
  color: #ff5f29;
}

.backdown {
  display: flex;
  position: absolute;
  width: 100%;
}

.left {
  width: 50%;
  background-color: #1d2939;
  height: 1500px;
  transition: transform 0.5s ease-in-out;
}

.right{
  width: 50%;
  background-color: #1d2939;
  height: 1500px;
  transition: transform 0.5s ease-in-out;
}

@media screen and (max-width: 992px){
  .render {
    max-width: 80%;
    padding-top: 10%;
  }
}

@media screen and (max-width: 767px){
  .render {
    padding-top: 25%;
  }
}

@media screen and (max-width: 479px){

}
</style>