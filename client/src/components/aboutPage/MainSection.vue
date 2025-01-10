<template>
  <ascii-render/>
  <!--    <div>Click to skip</div>-->

  <div class="about-page">
    <div class="main-block">

      <h1 class="heading-xlarge">{{ text.title }}</h1>
      <div class="about-container clearfix ">
        <img :src="`${frontendURL}/images/about.png`" alt="Me in about page of kajimacode"
             class="float-left"
             loading="lazy">
        <div class="about-text" v-html="text.about_text"></div>
      </div>
    </div>

    <!-- TODO CREATE CV AND ENABLE BLOCK -->
<!--        <resume-section :text="text" />-->
  </div>


</template>

<script>

import AsciiRender from "./AsciiRender.vue";
import ResumeSection from "./ResumeSection.vue";

export default {
  name: "MainSection",
  inject: [
    'backendURL',
    'frontendURL'
  ],
  components: {
    AsciiRender,
    ResumeSection
  },
  props: [
    'text'
  ],
}
</script>

<style>
.about-text b {
  color: #ff5f29;
  transition: color 0.2s ease-in-out;
}

.about-text a {
  text-decoration: none;
  color: white;
}

.about-text a > b:hover {
  color: #ff4000;
}
</style>

<style scoped>

.about-page {
  background-color: #1d2939;
}

.main-block {
  padding: 12.5vh 2rem 2rem 2rem;
  max-width: 90rem;
  margin-left: auto;
  margin-right: auto;
  min-height: 100vh;
}

.heading-xlarge {
  margin-top: 2rem;
  color: white;
}

.about-container {
  text-align: justify;
  background-image: linear-gradient(62deg, #344054, #1d2939);
  border-radius: 25px;
  color: white;
  max-width: 80rem;
  /*margin-left: auto;*/
  /*margin-right: auto;*/
  font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Fira Sans', 'Droid Sans', 'Helvetica Neue', sans-serif;
  font-size: 1rem;
  line-height: 1.5;
  letter-spacing: normal;
  padding: 4rem;
  margin: 2rem;
}

.clearfix:after {
  content: "";
  display: table;
  clear: both;
}

.float-left {
  float: left;
  margin-right: 70px;
  max-width: 43vh;
}

@media screen and (max-width: 992px) {
  .render {
    max-width: 80%;
    padding-top: 10%;
  }

  .float-left {
    margin-right: 45px;
    max-width: 16rem;
  }
}

@media screen and (max-width: 767px) {
  .render {
    padding-top: 25%;
  }

  .float-left {
    margin-right: 0;
    max-width: 18rem;
  }

  .about-container {
    display: flex;
    flex-direction: column-reverse;
    align-items: center;
    padding: 2rem;
    margin: 2rem 1rem 1rem;
  }

  .main-block {
    padding: 9vh 1rem 2rem 1rem;
  }
}

@media screen and (max-width: 479px) {

}

</style>