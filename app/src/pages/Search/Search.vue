<template>
<div class="border-solid border-2 rounded-md border-black w-5/6 m-auto mt-10 p-5" id="justify-center">
  
  <div class="">
    <p class="text-2xl">Let's Find The Route You Are Looking For.</p>
    <p class="text-xl">Select Your Route Information Below.</p>
  </div>

  <div class="flex m-10">
    <div class="flex-1"> 
      <p class="text-left ml-20 pl-5"> From </p>
      <input type="text" v-model="Departure.Name" v-on:keyup="findDeparture" @click="Departure.Selected=true;Arrival.Selected=false;" placeholder="Departing" class="shadow appearance-none border rounded w-2/3 p-3"/>
    </div>
    <div class="flex-1"> 
      <p class="text-left ml-20 pl-5"> To </p>
      <input type="text" v-model="Arrival.Name" v-on:keyup="findArrival" @click="Arrival.Selected=true;Departure.Selected=false;" placeholder="Arriving" class="shadow appearance-none border rounded w-2/3 p-3"/>
    </div>
  </div>

  <div class="flex m-10">
    <div class="flex-1"> 
      <p class="text-left ml-20 pl-5">Date </p>
      <input type="date" v-model="Departure.Date" class="shadow appearance-none border rounded w-2/3 p-3"/>
    </div>
    <br>
    <div class="flex-1"> 
      <p class="text-left ml-20 pl-5">Time </p>
      <input type="time" v-model="Departure.Time" class="shadow appearance-none border rounded w-2/3 p-3"/>
    </div>
  </div>

  <div class="">
    <br>
    <input type="submit" @click="search" class="shadow appearance-none border rounded w-2/3 p-3 m-5"/>
  </div>

  <div v-if="Departure.Selected==true"> 
    <div v-for="result in Results" :key="result.bpuic" class="">
      <hr>
      <a href="#" @click="Departure.StationID=result.fields.bpuic;Departure.Name=result.fields.bezeichnung_offiziell;Departure.Selected=false;">
      <p>Station ID: {{ result.fields.bpuic }}</p>
      <p class="text-xl">Station Name: {{ result.fields.bezeichnung_offiziell }}</p>
      <p>Station Code: {{result.fields.abkuerzung}}</p>
      <p>District: {{ result.fields.bezirksname }}</p>
      <p>City/Village: {{ result.fields.gemeindename }}</p>
      <p>Provider: {{ result.fields.go_abkuerzung_de }}</p>
      <p>Coordinates: {{ result.fields.geopos }}</p>
      <p>Canton Name: {{ result.fields.kantonsname }}</p>
      <p>Country: {{ result.fields.land_iso2_geo }}</p>
      </a>
    </div>
    <div v-if="(Results == null && Departure.Name != null) || Results == undefined || Results.length==0 ">
      <p>No Station Found</p>
    </div>
  </div>

  <div v-if="Arrival.Selected==true">
    <div v-for="result in Results" :key="result.bpuic" class="">
      <hr>
      <a href="#" @click="Arrival.StationID=result.fields.bpuic;Arrival.Name=result.fields.bezeichnung_offiziell;Arrival.Selected=false;">
      <p>Station ID: {{ result.fields.bpuic }}</p>
      <p class="text-xl">Station Name: {{ result.fields.bezeichnung_offiziell }}</p>
      <p>Station Code: {{result.fields.abkuerzung}}</p>
      <p>District: {{ result.fields.bezirksname }}</p>
      <p>City/Village: {{ result.fields.gemeindename }}</p>
      <p>Provider: {{ result.fields.go_abkuerzung_de }}</p>
      <p>Coordinates: {{ result.fields.geopos }}</p>
      <p>Canton Name: {{ result.fields.kantonsname }}</p>
      <p>Country: {{ result.fields.land_iso2_geo }}</p>
      </a>
    </div>
    <div v-if="(Results == null && Arrival.Name != null) || Results == undefined || Results.length==0 ">
      <p>No Station Found</p>
    </div>

  </div>
  <br>
</div>
</template>
<!--| |-->
<script lang="ts">
import { defineComponent } from 'vue';
import axios from 'axios';
export default defineComponent({
    name: 'Home',
    components: {

    },
    data() {
    const Arrival = <any | null>(null)
    const Departure = <any | null>(null)
    const Results = <any | null>(null)
      return {
        Arrival:{
          Selected:false,
          StationID:null,
          Name:null
        },
        Departure:{
          Selected:false,
          StationID:null,
          Name:null,
          Date:null,
          Time:null
        },
        Results
      };
    },
    methods: {
        findDeparture: async function(){
          this.Results = null;
          await this.findStation(this.Departure.Name);
        },
        findArrival: async function(){
          this.Results = null;
          await this.findStation(this.Arrival.Name);
        },
        findStation: async function(searchName: string) {
          let URI = "https://data.sbb.ch/api/records/1.0/search/?dataset=dienststellen-gemass-opentransportdataswiss&q="+searchName+"&rows=5&facet=abkuerzung&facet=gemeindename&facet=bezirksname&facet=kantonskuerzel&facet=land_iso2_geo&facet=bp_art_bezeichnung_de&facet=bpvh_verkehrsmittel_text_de&facet=go_abkuerzung_de&facet=is_haltestelle&facet=is_bedienpunkt&facet=is_verkehrspunkt&exclude.is_haltestelle=0&exclude.is_bedienpunkt=0&exclude.is_verkehrspunkt=0";
          let search = await axios.get(URI);
          this.Results = (search.data.records);
        },
        validateSearch: async function(){
          const Errors = [];
          if (this.Departure.StationID==null||undefined||""){
            Errors.push('Invalid Departure Station');
          }
          if (this.Arrival.StationID==null||undefined||""){
            Errors.push('Invalid Arrival Station');
          }
          //
          if(Errors.length>0){
            return Errors;
          }else{
            return 200;
          }
        },
        async search(){
          if(await this.validateSearch()!=200){
            throw Error;
          }else{
            console.log(this.Departure);
            console.log(this.Arrival)
            this.$router.replace({path:("/results/"+this.Departure.Date+"&"+this.Departure.Time+"&"+this.Departure.StationID+"&"+this.Arrival.StationID)})
          }
        }

    },
    setup() {

    },
    async created() {

    },
})
</script>
<!--| |-->
<style scoped>

</style>

