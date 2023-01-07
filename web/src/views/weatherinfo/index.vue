<template>

  <div class="main_div" style="padding: 40px;background-color: #fff;height100%;">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@3.4.1/dist/css/bootstrap.min.css"
      integrity="sha384-HSMxcRTRxnN+Bdg0JdbxYKrThecOKuH5zCYotlSAcp1+c8xmyTe9GYg1l9a69psu" crossorigin="anonymous">

    <h3>Pick Dates: </h3>
    <br>
    <div style="margin: 20px;">
      <strong>From: </strong>
      <input type="date" id="fromDate" name="fromDate" v-model="fromDate"  v-bind:max="today" >
      <strong style="margin-left: 20px;">To: </strong>
      <input type="date" id="toDate" name="toDate"  v-model="toDate"  v-bind:max="today" v-bind:min="fromDate">

      <button style="margin-left: 10px;" type="button" id="submitButton" v-on:click="getDataForRange()">Submit</button>
      <button style="margin-left: 30px;" v-on:click="getAllRecords();">Show All Records</button>

      <br>
      <br>

    </div>

    <table  class="table" >
      <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col">Temperature in Degree Celcius</th>
          <th scope="col">Date Recorded</th>

        </tr>
      </thead>
      <tbody id="tableBody">
        <tr v-for="(item, index) in listItems">
          <td>{{ (index + 1) }}</td>
          <td>{{ item.temperature }}</td>
          <td>{{ item.date_recorded }}</td>
        </tr>
      </tbody>
    </table>




  </div>

</template>
  
<script>
const urlPrefix = '/api/system/weatherinfo/'
import { request } from '@/api/service'
export default {
  name: 'weatherinfo',

  data() {
    return {
      listItems: [],
      today: new Date().toISOString().substr(0, 10),
      fromDate: new Date().toISOString().substr(0, 10),
      toDate: new Date().toISOString().substr(0, 10),
    }

  },
  methods: {
    getAllRecords() {
      this.listItems = []
      var address = this;
      request({ url: urlPrefix + 'all_records/', method: 'get', }).then(function (data) { address.listItems = data });
    },
    getDataForRange()
    {
      this.listItems = []
      var address = this;
      var queryparams = {}
      queryparams.from_date = this.fromDate
      queryparams.to_date = this.toDate
      request({ url: urlPrefix + 'get_by_range/', method: 'get', params:queryparams }).then(function (data) { address.listItems = data });


    }

  }, created() {
    var address = this;
    request({ url: urlPrefix + 'all_records/', method: 'get', }).then(function (data) { address.listItems = data });


  }, watch: {
    fromDate: function (newValue, oldValue) {
      this.toDate = this.today;
      // toDate.min = newDate;

    }
  }
  , mounted() {


    // var fromDateInput = document.getElementById("fromDate");
    // var toDateInput = document.getElementById("toDate");

    // fromDateInput.value = this.today;
    // toDateInput.value = this.today;
    






  }
}



</script>


