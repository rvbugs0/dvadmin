<template>

    <div class="main_div" style="height: 100%; padding: 40px;background-color: #fff;">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@3.4.1/dist/css/bootstrap.min.css" integrity="sha384-HSMxcRTRxnN+Bdg0JdbxYKrThecOKuH5zCYotlSAcp1+c8xmyTe9GYg1l9a69psu" crossorigin="anonymous">

        <h3>Pick Dates: </h3>  
        <br>
        <div style="margin: 20px;">
            <strong>From: </strong>
            <input type="date" id="fromDate" name="fromDate" onchange="fromChanged(this.value)">
            <strong style="margin-left: 20px;">To: </strong>
            <input type="date" id="toDate" name="toDate">

            <button style="margin-left: 10px;" type="button" id="submitButton" onclick="getForDates()">Submit</button>
            <button style="margin-left: 30px;" v-on:click="getAllRecords();">Show All Records</button>
            
            <br>
            <br>
        
        </div>

        <table class="table">
  <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">Temperature in Degree Celcius</th>
      <th scope="col">Date Recorded</th>
      
    </tr>
  </thead>
  <tbody id="tableBody">
    <tr v-for="(item,index) in listItems">
        <td>{{ (index+1) }}</td>
        <td>{{ item.temperature }}</td>
        <td>{{ item.date_recorded }}</td>
    </tr>
  </tbody>
</table>

        </div>

  </template>
  
  <script>
import { async } from 'q';

  export default {
    name: 'weatherinfo',
    
    data () {
      return {

        listItems : [{temperature:29,"date_recorded":"2022"}]


      }
    },
    methods: {
            async getAllRecords(){
            const res = await fetch("/weather_info_all_records");
            const finalRes = await res.json();
            this.listItems = finalRes;
            


        }
    }
  }


  
  




</script>
