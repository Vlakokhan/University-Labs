package com.example.projectmenu.data
import com.example.projectmenu.data.model.ApiInfo
interface InfoCallback {
    fun onSuccess(info: ApiInfo)
    fun onFailure()
}