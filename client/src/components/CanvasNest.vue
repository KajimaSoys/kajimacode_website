<template>
  <div
      ref="canvasNestContainer"
      class="canvas-nest-container"
      :style="{height: this.height}"
  >
    <canvas ref="canvas" class="canvas-nest"></canvas>
  </div>
</template>

<script>
// Same animation as canvas-nest.js, but the canvas only covers the viewport:
// points move across the whole container, only the visible part is drawn
const POINT_MAX = 6000;     // squared distance at which points link
const CURSOR_MAX = 20000;   // squared distance at which points link to the cursor
const COLOR = '0,0,0';
const POINT_COLOR = 'rgba(0,0,0)';

export default {
  name: 'CanvasNestComponent',
  props: {
    height: {
      default: '100vh',
      type: String
    },
    count: {
      default: 100,
      type: Number
    }
  },
  mounted() {
    this.initCanvasNest();
  },
  beforeUnmount() {
    cancelAnimationFrame(this.frame);
    this.resizeObserver.disconnect();
    window.removeEventListener('resize', this.resizeCanvas);
    window.removeEventListener('mousemove', this.onMouseMove);
    window.removeEventListener('mouseout', this.onMouseOut);
  },
  methods: {
    initCanvasNest() {
      const container = this.$refs.canvasNestContainer;
      this.ctx = this.$refs.canvas.getContext('2d');
      this.width = container.clientWidth;
      this.containerHeight = container.clientHeight;
      this.points = Array.from({length: this.count}, () => ({
        x: Math.random() * this.width,
        y: Math.random() * this.containerHeight,
        xa: 2 * Math.random() - 1,
        ya: 2 * Math.random() - 1,
        max: POINT_MAX
      }));
      this.cursor = {x: null, y: null, max: CURSOR_MAX};
      this.all = this.points.concat([this.cursor]);

      this.resizeObserver = new ResizeObserver(() => {
        this.width = container.clientWidth;
        this.containerHeight = container.clientHeight;
      });
      this.resizeObserver.observe(container);
      window.addEventListener('resize', this.resizeCanvas);
      window.addEventListener('mousemove', this.onMouseMove);
      window.addEventListener('mouseout', this.onMouseOut);
      this.resizeCanvas();

      this.frame = requestAnimationFrame(this.draw);
    },

    resizeCanvas() {
      const canvas = this.$refs.canvas;
      canvas.width = document.documentElement.clientWidth;
      canvas.height = window.innerHeight;
    },

    onMouseMove(e) {
      const container = this.$refs.canvasNestContainer;
      this.cursor.x = e.clientX - container.offsetLeft + document.scrollingElement.scrollLeft;
      this.cursor.y = e.clientY - container.offsetTop + document.scrollingElement.scrollTop;
    },

    onMouseOut() {
      this.cursor.x = null;
      this.cursor.y = null;
    },

    draw() {
      const ctx = this.ctx;
      const canvas = this.$refs.canvas;
      const width = this.width;
      const height = this.containerHeight;
      const cursor = this.cursor;
      const all = this.all;
      const rect = this.$refs.canvasNestContainer.getBoundingClientRect();
      // visible band of the container in its own coordinates, widened by the longest possible link
      const margin = Math.sqrt(CURSOR_MAX);
      const top = -rect.top - margin;
      const bottom = -rect.top + canvas.height + margin;

      ctx.setTransform(1, 0, 0, 1, 0, 0);
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      ctx.setTransform(1, 0, 0, 1, rect.left, rect.top);
      // a fixed canvas isn't clipped by the container, keep the drawing inside it
      ctx.save();
      ctx.beginPath();
      ctx.rect(0, 0, width, height);
      ctx.clip();
      ctx.fillStyle = POINT_COLOR;

      this.points.forEach((r, idx) => {
        r.x += r.xa;
        r.y += r.ya;
        r.xa *= r.x > width || r.x < 0 ? -1 : 1;
        r.ya *= r.y > height || r.y < 0 ? -1 : 1;
        const visible = r.y > top && r.y < bottom;
        if (visible) {
          ctx.fillRect(r.x - 0.5, r.y - 0.5, 1, 1);
        }
        // links of an off-screen point can't reach the screen, only the cursor pull still applies
        for (let i = visible ? idx + 1 : all.length - 1; i < all.length; i++) {
          const e = all[i];
          if (e.x === null || e.y === null) {
            continue;
          }
          const xDist = r.x - e.x;
          const yDist = r.y - e.y;
          const dist = xDist * xDist + yDist * yDist;
          if (dist < e.max) {
            if (e === cursor && dist >= e.max / 2) {
              r.x -= 0.03 * xDist;
              r.y -= 0.03 * yDist;
            }
            if (visible) {
              const d = (e.max - dist) / e.max;
              ctx.beginPath();
              ctx.lineWidth = d / 2;
              ctx.strokeStyle = `rgba(${COLOR},${d + 0.2})`;
              ctx.moveTo(r.x, r.y);
              ctx.lineTo(e.x, e.y);
              ctx.stroke();
            }
          }
        }
      });
      ctx.restore();
      this.frame = requestAnimationFrame(this.draw);
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

.canvas-nest {
  display: block;
  position: fixed;
  top: 0;
  left: 0;
  pointer-events: none;
  z-index: -1;
  opacity: 0.5;
}
</style>
