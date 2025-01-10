<template>
  <div
      ref="canvasNestContainer"
      class="canvas-nest-container"
      :style="{height: this.height}"
  ></div>
</template>

<script>
import CanvasNest from 'canvas-nest.js';

export default {
  name: 'CanvasNestComponent',
  props: {
    height: {
      default: '100vh'
    }
  },
  mounted() {
    this.initCanvasNest();
  },
  beforeUnmount() {
    if (this.canvasNestInstance) {
      this.canvasNestInstance.destroy();
    }
  },
  methods: {
    initCanvasNest() {
      const config = {
        color: '0,0,0',
        count: 250
      };
      this.canvasNestInstance = new CanvasNest(this.$refs.canvasNestContainer, config);
    }
  }
};
</script>

<style scoped>
.canvas-nest-container {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  z-index: -1;
  overflow: hidden;
}
</style>
