<template>
  <div>
    <video autoplay muted loop id="myVideo">
      <source src="../assets/AnimationBackground.mp4" type="video/mp4">
    </video>
    <div class="content">
      <v-file-input
        placeholder="Pick an image"
        outlined 
        dark
        autofocus
        prepend-icon="mdi-camera"
        class="input-text"
        background-color="#1976d2"
        @change="getFileName($event)"
      ></v-file-input>
      <v-btn @click="sendImage()" :loading="dialog" >PREDICT IMAGE</v-btn>

      <v-dialog
      v-model="dialog"
      hide-overlay
      persistent
      transition="dialog-top-transition"
      max-width="600"
    >
       <template>
        </template>
        <template v-slot:default="dialog">
          <v-card>
            <v-toolbar
              color="primary"
              dark
              class="text-h4"
            >Predicted sign </v-toolbar>
            <v-card-text>
              <div class="text-h2 pa-12">{{ predictedImage }}</div>
            </v-card-text>
            <v-card-actions class="justify-end">
              <v-btn
                text
                @click="dialog.value = false"
              >Close</v-btn>
            </v-card-actions>
          </v-card>
        </template>
    </v-dialog>
  </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'PredictionSite',

  data: () => ({
    imageName: null,
    predictedImage: null,
    dialog: false
  }),
  watch: {
    dialog (val) {
      if (!val) return

      setTimeout(() => (this.dialog = false), 5000)
    },
  },
  methods: {
    getFileName(e) {
      this.imageName = e.name;
  },
    sendImage() {
      const dataForm = new FormData();
      const path = 'http://localhost:5000/predict';

      dataForm.append('imagePath', this.imageName);
      
      axios.post(path, dataForm )
        .then((res) => {
          this.predictedImage = res.data;
          this.dialog = true;
        })
        .catch((error) => {
          console.error(error);
        });
    }
  
  },
}
</script>

<style>
#myVideo {
  position: fixed;
  right: 0;
  bottom: 0;
  min-width: 100%;
  min-height: 100%;
  z-index: 0;
}

.content {
  position: absolute; 
  top: 50%;
  left: 0; 
  right: 0; 
  margin-left: auto; 
  margin-right: auto; 
  width: 300px;
  text-align: center;
}

.v-file-input__text--placeholder {
  color: rgb(255, 255, 255);
  font-size: 1.2rem;
  font-weight: bold;
}

</style>