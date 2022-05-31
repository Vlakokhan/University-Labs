package com.example.lab4.di

import com.example.lab4.data.IDataSource
import com.example.lab4.data.api.OrderApiService
import com.example.lab4.data.api.RetrofitApiHelper
import com.example.lab4.ui.MainContract
import com.example.lab4.ui.MainPresenter

class DiHelper {
    companion object {

        var retrofitApiHelper: RetrofitApiHelper? = null
        var orderApiService: OrderApiService? = null

        fun getRetrofitHelper(): RetrofitApiHelper {
            if (retrofitApiHelper == null) {
                retrofitApiHelper = RetrofitApiHelper()
            }
            return retrofitApiHelper!!
        }

        fun getIDataSource(): IDataSource {
            if (orderApiService == null) {
                orderApiService = OrderApiService()
            }
            return orderApiService!!
        }
        fun getMainPresenter(view:MainContract.View): MainContract.Presenter {
            return MainPresenter(view, getIDataSource())

        }
    }
}