<template>
  <div class="main">
    <div class="navbar-block">
      <div class="logo">
        <svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
          <text x="10" y="30" class="text-tag-white">
            &#60;Kajima
          </text>
          <text x="50" y="30" class="text-tag-red">
            Code
          </text>
          <text  x="75" y="30" class="text-tag-white">
            />
          </text>
        </svg>
      </div>

      <div class="navbar-item">
        About
      </div>

      <div class="navbar-item">
        My skills
      </div>

      <div class="navbar-item">
        Work
      </div>

      <div class="navbar-item">
        Contact
      </div>
    </div>

    <div class="text-block">
      <div class="title">
        <h1>Hi, i'm kajimasoys!</h1>
      </div>

      <div class="description">
        This site is my portfolio
      </div>
    </div>

    <div class="render-block">
      <AsciiRender/>
    </div>
  </div>
</template>

<script>
import AsciiRender from "@/components/mainPage/AsciiRender.vue";

export default {
  name: "MainView",
  components: {
    AsciiRender,
  }
}
</script>


<style>
.main {
  display: flex;
}

.navbar-block {
  background: #202123;
  height: 100vh;
  width: 9.6%;
  /*max-width: 14.6%;*/
  color: white;
}

.logo {
  padding-bottom: 50px;
}

text {
  font-size: 11px;
}

.text-tag-red{
  fill: red;
}

.navbar-item{
  padding: 40px 20px;
  text-align: center;
}

.text-block {
  background: #e7e1d6;
  /*height: 969px;*/
  width: 28.5%;
  /*max-width: 14.6%;*/
  color: black;
}

.render-block {
  background: linear-gradient(180deg, #202123, #b86e48 53%, #db7b55 76%);
background: #ff8d60;  /* fallback for old browsers */
background: -webkit-linear-gradient(to bottom, #202123, #4c362f, #a36047, #ff8d60);  /* Chrome 10-25, Safari 5.1-6 */
background: linear-gradient(to bottom, #202123, #4c362f, #a36047, #ff8d60); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */

  /*height: 969px;*/
  width: 63%;
  /*max-width: 14.6%;*/
  color: black;
}

.render {
  margin-top: 15%;
}

</style>