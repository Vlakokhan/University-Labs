package com.example.lab4.data.api

import com.example.lab4.data.IDataSource
import com.example.lab4.data.model.ApiInfo
import com.example.lab4.di.DiHelper
import okhttp3.OkHttpClient
import okhttp3.logging.HttpLoggingInterceptor
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory

class OrderApiService: IDataSource {

    companion object {
        const val MASTER_KEY: String = "\$2b\$10\$HmcvDAa9iO7WHJkRgm2gx..6oJWeZJ46r4/iM8NjNcKB44MH2NiYG"
        const val ACCESS_KEY: String = "\$2b\$10\$MlQWlWU6/VmKPP2JJGxZ2eqnfn9YwIwP4wd/Gb/VdHCOBmXoo3KTm"
    }

    var api: OrderApi

    init {
        val retrofit = DiHelper.getRetrofitHelper().retrofit
        api = retrofit.create(OrderApi::class.java)
    }

    override fun getInfo(callback:IDataSource.InfoCallback) {
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



}
