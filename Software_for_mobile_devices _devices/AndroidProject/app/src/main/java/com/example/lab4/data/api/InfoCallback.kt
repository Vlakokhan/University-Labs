package com.example.lab4.data.api

import com.example.lab4.data.model.ApiInfo

interface InfoCallback {
    fun onSuccess(info: ApiInfo)
    fun onFailure()
}