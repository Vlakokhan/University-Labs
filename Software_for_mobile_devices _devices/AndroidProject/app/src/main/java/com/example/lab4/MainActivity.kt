package com.example.lab4

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.widget.TextView
import com.example.lab4.data.api.OrderApiService
import com.example.lab4.data.model.ApiInfo
import com.example.lab4.data.model.OrderData

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
    }
    override fun onResume() {
        super.onResume()
        loadData()
    }


    private fun loadData() {
        Log.d("API", "loadData")
        val service = OrderApiService()
        service.getInfo(object : OrderApiService.InfoCallback {
            override fun onSuccess(info: ApiInfo) {
                displayInfo(info.record)
            }
            override fun onFailure() {
            }
        })
    }
    private fun displayInfo(orderDish: OrderData) {
        val categoryTextView: TextView = findViewById(R.id.category)
        val nameTextView: TextView = findViewById(R.id.DishName)
        val priceTextView: TextView = findViewById(R.id.Price)
        val weightTextView: TextView = findViewById(R.id.Weight)
        val amountTextView: TextView = findViewById(R.id.Amount)
        Log.d("API", orderDish.category)
        Log.d("API", orderDish.name)
        Log.d("API", orderDish.price)
        Log.d("API", orderDish.weight)
        Log.d("API", orderDish.amount)
        categoryTextView.text = "category: ${ orderDish.category}"
        nameTextView.text = "DishName: ${orderDish.name}"
        priceTextView.text = "Price: ${orderDish.price}"
        weightTextView.text = "Weight: ${orderDish.weight}"
        amountTextView.text = "Amount: ${orderDish.amount}"
    }
}