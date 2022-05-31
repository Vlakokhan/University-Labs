package com.example.lab4.data

import com.example.lab4.data.model.ApiInfo

interface IDataSource {
     fun getInfo(callback: InfoCallback)
     interface InfoCallback {
        fun onSuccess(info: ApiInfo)
        fun onFailure()
    }
}