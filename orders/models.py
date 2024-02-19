from django.db import models

from goods.models import Products
from users.models import User


class OrderItemQueryset(models.QuerySet):
    def total_price(self):
        return sum(cart.products_prise() for cart in self)

    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0


class Order(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.SET_DEFAULT, null=True, blank=True, verbose_name="Пользователь",
                             default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания заказа", )
    phone_number = models.CharField(max_length=20, verbose_name="Номер телефона", )
    requires_delivery = models.BooleanField(verbose_name="Требуется доставка", default=False)
    delivery_address = models.TextField(null=True, blank=True, verbose_name="Адрес доставки", default=None)
    payment_on_get = models.BooleanField(verbose_name="оплата при получении", default=False)
    is_paid = models.BooleanField(verbose_name="Оплачено", default=False)
    status = models.CharField(max_length=50, verbose_name="Статус заказа", default="в оработке")

    class Meta:
        db_table = "order"
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return f"Заказ № {self.pk} | Покупатель {self.user.first_name} {self.user.last_name}"


class OrderItem(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE, verbose_name="Заказ", )
    product = models.ForeignKey(to=Products, on_delete=models.SET_DEFAULT, verbose_name="Товар",
                                default=None, null=True)
    name = models.CharField(max_length=120, verbose_name="Название", )
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Цена", )
    quantity = models.PositiveIntegerField(verbose_name="Количество", default=0)
    created_timestamp = models.DateTimeField(verbose_name="Дата продажи", auto_now_add=True)

    class Meta:
        db_table = "order_item"
        verbose_name = "Проданный товар"
        verbose_name_plural = "Проданные товары"

    objects = OrderItemQueryset.as_manager()

    def products_price(self):
        return round(self.product.sell_price() * self.quantity, 2)

    def __str__(self):
        return f"Товар {self.name} |  Заказ № {self.order.pk}"
