<template>
    <h6> This is the Projects page. This page displays all repositories of the user. I will be using <a
            href="https://docs.github.com/en/rest/repos/repos?apiVersion=2022-11-28#list-organization-repositories"
            target="_blank">List organization repositories API</a>. Most information in this page will be clickable. Now its just hard coded.  </h6>
    <div class="container">
        <p class="container-title">Here are Your Projects </p>

        <div class="gradient-cards">
            <div class="card">
                <div class="container-card">

                    <p class="card-title">SE577-Project </p>
                    <p class="card-description">My course project for SE577 Software Architecture goes here. The course
                        project will involve building a web based, cloud native, front end to GitHub.</p>
                    <div class="info">
                        <ul>
                            <li>5 Issues</li>
                            <li>13 Forks</li>
                            <li>Vue</li>

                        </ul>
                    </div>
                </div>
            </div>

            <div class="card">
                <div class="container-card ">

                    <p class="card-title">FlashRewind</p>
                    <p class="card-description">A Flashcard-based Study Tool</p>
                    <div class="info">
                        <ul>
                            <li>5 Issues</li>
                            <li>13 Forks</li>
                            <li>Python</li>

                        </ul>
                    </div>
                </div>
            </div>

            <div class="card">
                <div class="container-card">

                    <p class="card-title">Hand tracker</p>
                    <p class="card-description">Program to track hand movements using mediapipe and open CV</p>
                    <div class="info">
                        <ul>
                            <li>5 Issues</li>
                            <li>13 Forks</li>
                            <li>Python</li>

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