<template>
    <div style="background-color:white">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@3.4.1/dist/css/bootstrap.min.css"
            integrity="sha384-HSMxcRTRxnN+Bdg0JdbxYKrThecOKuH5zCYotlSAcp1+c8xmyTe9GYg1l9a69psu" crossorigin="anonymous">
        <div class="container">
            <br>

            <br>


            <!-- <a style="font-size: large;" href="/index">Go Back</a> -->
            <h2>Average Temperature Data for the year 2022</h2>
            <br>
            <div id="container" style="height: 480px;"></div>
        </div>

    </div>


</template>
  
<script>
import * as echarts from '../static/echarts.min'
const urlPrefix = '/api/system/weatherinfo/'
import { request } from '@/api/service'
export default {
    name: 'charview',
    data() {
        return {
            results: []
        }

    },
    methods: {

    }, mounted() {

        var dom = document.getElementById('container');
        var myChart = echarts.init(dom, null, {
            renderer: 'canvas',
            useDirtyRect: false
        });

        this.option = {
            title: {
                text: 'Month vs Average Temperature in Degree Celcius',
                left: 'center'
            },
            xAxis: {
                type: 'category',
                data: []
            },
            yAxis: {
                type: 'value'
            },
            series: [
                {
                    data: [],
                    type: 'line'
                }
            ]
        };

        this.results = []
        var address = this;
        request({ url: urlPrefix + 'get_average_temperatures/', method: 'get', }).then(function (finalRes) {

            address.results = finalRes;

            for (var i in finalRes) {
                address.option.xAxis.data.push(finalRes[i].month);

                address.option.series[0].data.push(finalRes[i].average_temp);
            }
            if (address.option && typeof address.option === 'object') {
                myChart.setOption(address.option);
            }


        });

        window.addEventListener('resize', myChart.resize);
    }

}



</script>


