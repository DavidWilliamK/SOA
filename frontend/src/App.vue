<template>
  <v-app class="app">
    <v-navigation-drawer
            app
            clipped
    >
      <v-list dense>
        <v-list-item link tag="router-link" :to="{name: 'home'}" :exact-active=false>
          <v-list-item-action>
            <v-icon>mdi-home</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Home Page</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item link tag="router-link" :to="{name: 'authors'}" :exact-active=false>
          <v-list-item-action>
            <v-icon>mdi-account-group-outline</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Authors</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-app-bar
      app
      color="primary"
      dark
      clipped-left
    >
      Simple Face Detection App
    </v-app-bar>
    <v-content class="main-content">
      <router-view></router-view>
    </v-content>
  </v-app>
</template>

<script>

export default {
  name: 'App',

  components: {
  },

  created () {
    this.$vuetify.theme.dark = true
  },

  data: () => ({
    //
  })
};
</script>

<style lang="scss" scoped>
  html, body {
    height: 100%;
    margin: 0;
    color: #505050;
    font-size: 100%;
    line-height: 1.4rem;
    font-family: 'Open Sans', Helvetica, Arial, sans-serif;
  }

  .app {
    display: flex;
    flex-direction: column;
    font-family: 'Open Sans', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
  }

  .main-content {
    padding-top: 0.5rem;
    padding-left: 0.5rem;
    padding-right: 9rem;
    width: 95vw;
  }
</style>
