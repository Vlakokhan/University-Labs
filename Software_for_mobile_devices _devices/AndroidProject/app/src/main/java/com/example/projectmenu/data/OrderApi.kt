package com.example.projectmenu.data
import com.example.projectmenu.data.model.ApiInfo
import retrofit2.Call
import retrofit2.http.GET
import retrofit2.http.Header

interface OrderApi {

    @GET("b/6294de17449a1f3821f61c17")
    fun getInfo(@Header("X-Master-Key") masterKey: String,
                @Header("X-Access-Key") accessKey: String):
            Call<ApiInfo>

}