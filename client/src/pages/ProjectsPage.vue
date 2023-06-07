<template>
    
    <div class="container">
        <p class="container-title">Here are Your Projects </p>

        <div class="gradient-cards">
            <div class="card" v-for="repo in repositoryData" :key="repo.id">
                <div class="container-card">
                    <p class="card-title">{{ repo.name }}</p>
                    <p class="card-description">{{ repo.description }}</p>
                    <div class="info">
                        <ul>
                            <li>{{ repo.open_issues }} Issues</li>
                            <li>{{ repo.forks }} Forks</li>
                            <li>{{ repo.language }}</li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
    
<script lang="ts">
export default {
    name: 'ProjectsPage',
};
</script>
    
<script setup lang="ts">
//Most code goes here
import { onMounted, ref } from 'vue';
import type { RepositoryApiInterface } from './ApiInterfaces';
import axios from 'axios';

let repositoryData = ref<RepositoryApiInterface[]>([]);

onMounted(async () => {
    let allReposURI = 'http://localhost:8080/repositories'
    let repositoryAPI = await axios.get<RepositoryApiInterface[]>(allReposURI)
    // If OK, set the repositoryData variable.
    if (repositoryAPI.status == 200) {
        repositoryData.value = repositoryAPI.data
    }
});
</script>
    
    <!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
body {
    background-color: black;
}

.container {
    width: 1200px !important;
    padding: 0 !important;
    margin-right: auto;
    margin-left: auto;

    @media screen and (min-width: 992px) and (max-width: 1439px) {
        max-width: 1279px !important;
        padding: 0 !important;
        margin: 0 80px !important;
        width: auto !important;
    }

    @media screen and (max-width: 991px) {
        max-width: 959px !important;
        margin: 0 16px !important;
        padding: 0 !important;
        width: auto !important;
    }
}

.gradient-cards {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 32px;
    padding: 30px;

    @media screen and (max-width: 991px) {
        grid-template-columns: 1fr;
    }
}



.card {
    max-width: 550px;
    border: 0;
    width: 100%;
    margin-inline: auto;
}

.container-card {
    position: relative;
    border: 2px solid transparent;
    background: linear-gradient(71deg, #080509, #1a171c, #080509);
    background-clip: padding-box;
    border-radius: 45px;
    padding: 40px;


}







.card-title {
    font-weight: 600;
    color: white;
    letter-spacing: -0.02em;
    line-height: 40px;
    font-style: normal;
    font-size: 28px;
    padding-bottom: 8px;
}

.card-description {
    font-weight: 600;
    line-height: 32px;
    color: hsla(0, 0%, 100%, 0.5);
    font-size: 16px;
    max-width: 470px;
}
</style>