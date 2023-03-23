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

    }
  },
  methods: {
    async get_ascii(){
      await axios
      .get('api/v1/get_ascii')
      .then(response => {

        this.ascii_array = response.data.res
        // console.log(this.ascii_array)
        this.fill_svg()

      })
      .catch(error => {
        console.log('Ошибка при загрузке ascii-фреймов')
        console.log('retrying..')
            setTimeout(() => {
              this.get_ascii()
            }, 2000)
      })
    },


    fill_svg(){
      let frames = this.ascii_array

      async function renderElementsWithDelay() {
        console.log('render started')
        for (const frame of frames) {
          let text_attrs = ''
          let i = 0

          frame.forEach(function (row){
            text_attrs = text_attrs + `<text x="0" y="${i}" style="font-size: 10.5202px; font-family: monospace; dominant-baseline: hanging; white-space: pre; fill: white;">${row}</text>`
            i += 13
          })

          document.getElementById("svg-container").innerHTML = text_attrs
          await new Promise(resolve => setTimeout(resolve, 30));
        }
        // renderElementsWithDelay();
        // console.log('render finished')

      }
      window.scrollTo({top:0,behavior:'auto'});
      renderElementsWithDelay().then(() => {
        this.stopAnimation()
      })

    },

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
    this.get_ascii()
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