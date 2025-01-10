<template>
  <div class="fullscreen">
    <canvas id="canvas3d"></canvas>
  </div>
</template>

<script>
import {Application} from '@splinetool/runtime';

export default {
  name: "SplineComponent",
  data() {
    return {
      // isMouseOverCanvas: true
    }
  },
  methods: {},
  mounted() {
    const canvas = document.getElementById('canvas3d');
    const app = new Application(canvas);
    // app.load('https://prod.spline.design/xIGHe114R6O9GUHU/scene.splinecode');
    app.load('https://prod.spline.design/T2IO8aOzLssJ5eJQ/scene.splinecode');
    //
    //
    //  canvas.addEventListener('mouseenter', () => {
    //   this.isMouseOverCanvas = true;
    //   console.log("мы внутри")
    // });
    //
    // canvas.addEventListener('mouseleave', () => {
    //   this.isMouseOverCanvas = false;
    //   console.log("мы вышли")
    // });

    document.addEventListener('mousemove', function (event) {
      if (event.target !== canvas) {
        // console.log('работаю')
        const rect = canvas.getBoundingClientRect();

        let x = 0
        if (document.documentElement.clientWidth <= 767) {
          x = event.clientX - rect.left
        } else {
          x = event.clientX - rect.left + 1000;
        }
        const y = event.clientY - rect.top;


        canvas.dispatchEvent(new PointerEvent('pointermove', {
          clientX: x,
          clientY: y,
          pointerType: 'mouse'
        }));
      }
    });

  }
}
</script>

<style scoped>
.fullscreen {
  width: 100%;
  height: 100%;
  position: relative;
  z-index: 1;
}
</style>