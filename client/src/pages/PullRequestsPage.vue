<template>
    <p class="container-title">Here are Your Open Pull Requests </p>
    
    <div class="row">
        <div class="card"  v-for="pr in prData" :key="pr.number">
            <h4>{{ pr.title }}</h4>
            <span class="nowrap">
                <form class="inlineForm">
                    <button class="button button1">SE-577 Project</button>

                </form>
            
            </span>
            
            <p>#{{ pr.number }} opened at {{ pr.created_at }} by lidaSusanSabu13</p>
            
        </div>
        
        
    </div>
</template>
    
<script lang="ts">
export default {
    name: 'PullRequestsPage',
};
</script>
    
<script setup lang="ts">
//Most code goes here
import { onMounted, ref } from 'vue';
import type { PrApiInterface } from './ApiInterfaces';
import axios from 'axios';

let prData = ref<PrApiInterface[]>([]);

onMounted(async () => {
    let allPrURI = 'http://localhost:8080/pr'
    let prAPI = await axios.get<PrApiInterface[]>(allPrURI)
    // If OK, set the repositoryData variable.
    if (prAPI.status == 200) {
        prData.value = prAPI.data
    }
});
</script>
    
    
    <!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>



@import url("https://fonts.googleapis.com/css?family=Poppins:100,100i,200,200i,300,300i,400,400i,500,500i,600,600i,700,700i,800,800i,900,900i&subset=devanagari,latin-ext");

* {
  padding: 0;
  margin: 0;
  box-sizing: border-box;
  font-family: "Poppins", sans-serif;
}

body {
  background-color: #343a40;
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  user-select: none;
}
.row{
    height: 700px;
}
.card {
  border-radius: 10px;
  filter: drop-shadow(0 5px 10px 0 #070c0a);
  width: 90%;
  
  background: linear-gradient(71deg, #080509, #1a171c, #080509);
  padding: 20px;
  position: relative;
  z-index: 0;
  overflow: hidden;
  transition: 0.6s ease-in;
  margin: 5%;
}

.card::before {
  content: "";
  position: absolute;
  z-index: -1;
  top: -15px;
  right: -15px;
  background: #4CAF50;
  height:220px;
  width: 25px;
  border-radius: 32px;
  transform: scale(1);
  transform-origin: 50% 50%;
  transition: transform 0.25s ease-out;
}



.card:hover{
    color: #ffffff;

}

.card p{
    padding: 10px 0;
}
.button {
  background-color: #4CAF50; /* Green */
  border: none;
  color: #4CAF50;
  padding: 3px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 11px;
  margin: 4px 2px;
  transition-duration: 0.4s;
  cursor: pointer;
}

.button1 {
  background-color: #4CAF50; 
  color: black; 
  border: 2px solid #4CAF50;
}

.button1:hover {
  background-color: #4CAF50;
  color: white;
}





</style>