<template>
  <div class="ascii-view">
    <div class="blur"/>
    <div class="background"/>
    <div class="greetings">
      Welcome to the world of web development! As a skilled web developer, I am here to help bring your online vision to life. Whether you're looking to create a new website, revamp an existing one, or add custom features to enhance user experience, I have the expertise to get the job done. My services include responsive design, e-commerce integration, and SEO optimization to ensure your website is not only beautiful but also functional and easy to find. Let's work together to take your online presence to the next level. Contact me today to discuss your project.
    </div>
    <div class="ascii">
      <ascii-render/>
    </div>

  </div>

</template>

<script>
import AsciiRender from "@/components/aboutPage/AsciiRender.vue";

export default {
    name: "AsciiView",
  components: {AsciiRender}
}
</script>

<style>
/*.image-box {*/
/*  position: absolute;*/
/*  left: 0;*/
/*  top: 0;*/
/*  height: 100%;*/
/*  z-index: -2;*/
/*}*/
.background {
  position: fixed;
  height: 1080px;
  width: 1920px;
  background: url(src/images/generated-bg.jpg);
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  z-index: -2;
}

.blur{
  position: fixed;
  height: 1080px;
  width: 1920px;
  background: rgba(6, 6, 31, 0.7);
  backdrop-filter: blur(6px);
  color: #ffffff;
  z-index: -1;
}

.greetings {

}

</style>