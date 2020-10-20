<template>
<div>
  <b-row>
    <b-col></b-col>
    <b-col><div>
    <b-input v-model="neu_fach" placeholder="Fach"></b-input>
    <b-form-spinbutton id="sb-step" placeholder="Note" v-model="neu_note" min="1" max="6" step="0.25"></b-form-spinbutton>
    <b-button variant="primary" class="w-100" @click="postNote">Eintragen</b-button>
</div></b-col>
    <b-col></b-col>
  </b-row>
  <br>
  <b-row>
    <b-col></b-col>
    <b-col><div v-for="note in noten" :key="note.id">  <b-list-group horizontal>
    <b-list-group-item class="w-100">{{ note.bezeichnung }}</b-list-group-item>
    <b-list-group-item>{{ note.notenwert }}</b-list-group-item>
  </b-list-group></div> </b-col>
    <b-col></b-col>
    </b-row>
</div>
</template>

<script>
import axios from "axios";
export default {
  name: "Fach",

  data() {
    return {
      noten: [],
      neu_fach: null,
      neu_note: null,
    };
  },
  mounted() {
    this.getNote();
  },
  methods: {
    async getNote() {
      console.log("hi");
      let response = await axios.get("/noten/");
      this.noten = response.data;
    },
    async postNote() {
      console.log("hi")
      let note = { bezeichnung: this.neu_fach, notenwert: this.neu_note};
      await axios.post("/noten/", note);
      let response = await axios.get("/noten/");
      this.noten = response.data;
      this.neu_fach = null
      this.neu_note = null
    },
  },
};
</script>

<style scoped>

</style>
