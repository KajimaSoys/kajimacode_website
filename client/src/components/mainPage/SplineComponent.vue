<template>
  <div class="fullscreen" ref="container"></div>
</template>

<script>
const SCENE_URL = 'https://prod.spline.design/T2IO8aOzLssJ5eJQ/scene.splinecode';
// const SCENE_URL = 'https://prod.spline.design/xIGHe114R6O9GUHU/scene.splinecode';

// The runtime never releases a disposed scene (its renderer stays subscribed to a module level object),
// so a single scene lives for the whole session and is only paused while the main page is closed
let scene = null;

async function getScene(container) {
  if (!scene) {
    scene = import('@splinetool/runtime').then(({Application}) => {
      // the runtime watches the canvas parent for size changes, so the parent moves between pages together with it
      const wrapper = document.createElement('div');
      wrapper.style.cssText = 'width: 100%; height: 100%;';
      const canvas = document.createElement('canvas');
      canvas.id = 'canvas3d';
      wrapper.appendChild(canvas);
      // the runtime reads the canvas size on start, so it has to be in the page already
      container.appendChild(wrapper);
      const app = new Application(canvas);
      app.load(SCENE_URL);
      return {app, canvas, wrapper};
    });
  }
  return scene;
}

export default {
  name: "SplineComponent",
  data() {
    return {
      // isMouseOverCanvas: true
    }
  },
  methods: {
    onMouseMove(event) {
      const canvas = this.canvas;
      if (event.target !== canvas) {
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
    }
  },
  async mounted() {
    // the runtime is heavy and only needed here, keep it out of the main bundle
    const {app, canvas, wrapper} = await getScene(this.$refs.container);
    if (this.unmounted) {
      // the page was left before the runtime arrived, keep the scene paused until the next visit
      app.stop();
      wrapper.remove();
      return;
    }
    this.app = app;
    this.canvas = canvas;
    this.wrapper = wrapper;
    this.$refs.container.appendChild(wrapper);
    if (app.isStopped) {
      app.play();
    }
    document.addEventListener('mousemove', this.onMouseMove);
  },
  beforeUnmount() {
    this.unmounted = true;
    document.removeEventListener('mousemove', this.onMouseMove);
    if (this.app) {
      this.app.stop();
      this.wrapper.remove();
    }
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