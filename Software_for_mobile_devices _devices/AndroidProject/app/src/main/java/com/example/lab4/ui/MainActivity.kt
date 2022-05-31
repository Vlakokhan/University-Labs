package com.example.lab4.ui

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.widget.TextView
import android.widget.Toast
import com.example.lab4.R
import com.example.lab4.data.model.ApiInfo
import com.example.lab4.di.DiHelper


class MainActivity : AppCompatActivity(), MainContract.View {
    private lateinit var presenter: MainContract.Presenter

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        initPresentor()
    }

    private fun initPresentor() {
        presenter = DiHelper.getMainPresenter(this)
    }

    override fun onResume() {
        super.onResume()
        presenter.loadData()
    }

        override fun displayInfo(info: ApiInfo) {
            val categoryTextView: TextView = findViewById(R.id.category)
            val nameTextView: TextView = findViewById(R.id.DishName)
            val priceTextView: TextView = findViewById(R.id.Price)
            val weightTextView: TextView = findViewById(R.id.Weight)
            val amountTextView: TextView = findViewById(R.id.Amount)
            Log.d("API", info.record.category)
            Log.d("API", info.record.name)
            Log.d("API", info.record.price)
            Log.d("API", info.record.weight)
            Log.d("API", info.record.amount)
            categoryTextView.text = "category: ${ info.record.category}"
            nameTextView.text = "DishName: ${info.record.name}"
            priceTextView.text = "Price: ${info.record.price}"
            weightTextView.text = "Weight: ${info.record.weight}"
            amountTextView.text = "Amount: ${info.record.amount}"
        }
        override fun displayError() {
            Toast.makeText(this, "Unable to load info", Toast.LENGTH_LONG).show()

        }
    }