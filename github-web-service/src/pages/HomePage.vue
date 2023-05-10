<template>
  <h6> This is the home page. This page displays information about the user using githubs <a
      href="https://docs.github.com/en/rest/users/users?apiVersion=2022-11-28#get-a-user" target="_blank">get a user
      API</a>. So this application should have a user Sign in and sign up right ?</h6>

  <div class="card-container">

    <img class="round" src="https://avatars.githubusercontent.com/u/25691275?v=4" alt="user" />
    <h3>Lida Susan Sabu</h3>
    <h6>lidasusansabu13</h6>
    <h6>lidasusansabu13@gmail.com</h6>
    <p>Python Developer and <br /> Software Designer</p>
    <div class="info">
      <ul>
        <li>5 Followers</li>
        <li>13 Following</li>
        <li>17 Repositories</li>
        
      </ul>
    </div>
   
  </div>
</template>
    
<script lang="ts">
export default {
  name: 'HomePage',
};
</script>
    
<script setup lang="ts">
    //Most code goes here
</script>
  
    
    <!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
@import url('https://fonts.googleapis.com/css?family=Montserrat');

* {
  box-sizing: border-box;
}

body {
  background-color: #28223F;
  font-family: Montserrat, sans-serif;

  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;

  min-height: 100vh;
  margin: 0;
}

h3 {
  margin: 10px 0;
}

h6 {
  margin: 5px 0;
  
}

p {
  font-size: 14px;
  line-height: 21px;
}

.card-container {
  background: linear-gradient(71deg, #080509, #1a171c, #080509);
  border-radius: 5px;
  box-shadow: 0px 10px 20px -10px rgba(0, 0, 0, 0.75);
  color: #dde5e1;

  position: relative;
  width: 1050px;
  max-width: 100%;
  text-align: center;
  padding: 30px;
  margin-left: 200px;
}

.card-container .pro {
  color: #231E39;
  background-color: #FEBB0B;
  border-radius: 3px;
  font-size: 14px;
  font-weight: bold;
  padding: 3px 7px;
  position: absolute;
  top: 30px;
  left: 30px;
}

.card-container .round {
  border: 1px solid #518756;
  border-radius: 50%;
  padding: 7px;
  max-width: 300px;
}




</style>