package com.example.lab4.ui
import com.example.lab4.data.model.ApiInfo

interface MainContract {
    interface View {
        fun displayInfo(info: ApiInfo)
        fun displayError()

    }
    interface Presenter {
        fun loadData()
    }


}