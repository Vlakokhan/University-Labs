package com.example.projectmenu.data

import com.example.projectmenu.data.model.ApiInfo
import okhttp3.OkHttpClient
import okhttp3.logging.HttpLoggingInterceptor
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory

class OrderApiService {

    companion object {
        const val MASTER_KEY: String = "\$2b\$10\$HmcvDAa9iO7WHJkRgm2gx..6oJWeZJ46r4/iM8NjNcKB44MH2NiYG"
        const val ACCESS_KEY: String = "\$2b\$10\$MlQWlWU6/VmKPP2JJGxZ2eqnfn9YwIwP4wd/Gb/VdHCOBmXoo3KTm"
    }

    var api: OrderApi

    init {
        val logging = HttpLoggingInterceptor()
        logging.setLevel(HttpLoggingInterceptor.Level.BODY)

        val client: OkHttpClient = OkHttpClient.Builder()
            .addInterceptor(logging)
            .build()

        val retrofit = Retrofit.Builder()
            .baseUrl("https://api.jsonbin.io/v3/")
            .client(client)
            .addConverterFactory(GsonConverterFactory.create())
            .build()
        api = retrofit.create(OrderApi::class.java)
    }

    fun getInfo(callback: InfoCallback) {
        api.getInfo(
            MASTER_KEY,
            ACCESS_KEY
        ).enqueue(object : Callback<ApiInfo> {
            override fun onResponse(
                call: Call<ApiInfo>, response:
                Response<ApiInfo>
            ) {
                if (response.code() == 200 && response.body() != null)
                    callback.onSuccess(response.body()!!)
                else
                    callback.onFailure()
            }

            override fun onFailure(call: Call<ApiInfo>, t: Throwable) {
                callback.onFailure()
            }
        })
    }
    interface InfoCallback {
        fun onSuccess(info: ApiInfo)
        fun onFailure()
    }
}