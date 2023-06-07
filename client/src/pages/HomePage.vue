<template>

  <div class="card-container">

    <img class="round" :src="userData.avatar_url" alt="user" />
    <h3>{{ userData.name }}</h3>
    <h6>{{ userData.login }}</h6>
    <h6>{{ userData.email }}</h6>
    <p>{{ userData.bio }}..</p>
    <div class="info">
      <ul>
        <li>{{ userData.followers }} Followers</li>
        <li>{{ userData.following }} Following</li>
        <li>{{ userData.public_repos }} Repositories</li>
        
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
import { onMounted, ref } from 'vue';
import type { UserApiInterface } from './ApiInterfaces';
import axios from 'axios';

let userData = ref<UserApiInterface[]>([]);

onMounted(async () => {
    let userURI = 'http://localhost:8080/user'
    let userAPI = await axios.get<UserApiInterface[]>(userURI)
    // If OK, set the userData variable.
    if (userAPI.status == 200) {
      userData.value = userAPI.data
    }
});
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