package com.example.projectmenu

import android.content.Intent
import android.os.Bundle
import android.util.Log
import android.view.View
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import com.example.projectmenu.data.OrderApiService
import com.example.projectmenu.data.model.ApiInfo
import com.example.projectmenu.data.model.OrderDish


class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

    }

    fun addMe(view: View) {
        val addMeIntent  =  Intent(this, DishSelection::class.java)
        startActivity(addMeIntent)
    }




}
