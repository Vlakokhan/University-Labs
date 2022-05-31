package com.example.lab4.ui

import android.util.Log
import com.example.lab4.data.IDataSource
import com.example.lab4.data.model.ApiInfo

    class MainPresenter(val view:MainContract.View,val service: IDataSource):MainContract.Presenter {

     override fun loadData() {
        Log.d("API", "loadData")

        service.getInfo(object : IDataSource.InfoCallback {
            override fun onSuccess(info: ApiInfo) {
                view.displayInfo(info)
            }
            override fun onFailure() {
                view.displayError()
            }
        })
    }
}