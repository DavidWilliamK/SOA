<template>
    <div class="home__container">
        <v-alert
                color="orange"
                dismissible
                transition="scale-transition"
                min-width="100%"
        >
            {{alertText}}
        </v-alert>
        <v-file-input
                v-model="files"
                color="deep-purple accent-4"
                counter
                label="File input"
                multiple
                placeholder="Select your files"
                prepend-icon="mdi-paperclip"
                outlined
                :show-size="1000"
        >
            <template v-slot:selection="{ index, text }">
                <v-chip
                        v-if="index < 2"
                        color="deep-purple accent-4"
                        dark
                        label
                        small
                >
                    {{ text }}
                </v-chip>

                <span
                        v-else-if="index === 2"
                        class="overline grey--text text--darken-3 mx-2"
                >
        +{{ files.length - 2 }} File(s)
      </span>
            </template>
        </v-file-input>
        <v-btn @click="detect">Submit</v-btn>
        <v-carousel v-if="!!files.length && !!detected.length">
            <v-carousel-item
                    v-for="(item,i) in detected"
                    :key="i"
                    :src="item.src"
                    reverse-transition="fade-transition"
                    transition="fade-transition"
            ></v-carousel-item>
        </v-carousel>
    </div>
</template>

<script type="text/javascript" src="./js/home.js">
</script>

<style lang="scss" scoped>
    .home {
        &__container {
            display: flex;
            flex-direction: column;
            justify-content: center;
            width: 100%;
            margin: 2rem
        }
    }
</style>