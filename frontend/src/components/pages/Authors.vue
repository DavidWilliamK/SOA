<template>
    <div class="authors">
        <div class="authors_dog">
            <img :src="imageSrc" alt="Something went wrong" class="authors_dog-image">
        </div>
        <div class="authors_data">

            <h1>Hi!</h1>
            <p>
                This simple page is brought to you by:
            </p>
            <ul>
                <li>Adithya Nugraha Tjokrosetio </li>
                <li>David William </li>
                <li>Kevin William Gunawan</li>
            </ul>
            <p>
                As the realization of a project for Service Oriented Architecture <br><br>
                There are 3 APIs used in this project: <br>
            </p>
            <ul>
                <li>FOAAS</li>
                <li>RandomDog</li>
                <li>Self-made object detection</li>
            </ul>
        </div>
    </div>
</template>

<script type="text/javascript" src="./js/authors.js">
</script>

<style scoped lang="scss">
    .authors{
        width: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: row;
        padding: 5rem;
        &_dog {
            margin-right: 10rem;
            &-image {
                width: 30rem;
            }
        }
        &_data {

        }
    }
</style>