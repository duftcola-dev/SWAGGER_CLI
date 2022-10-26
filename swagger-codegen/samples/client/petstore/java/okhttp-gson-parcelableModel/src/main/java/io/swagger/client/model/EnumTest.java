/*
 * Swagger Petstore
 * This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\
 *
 * OpenAPI spec version: 1.0.0
 * Contact: apiteam@swagger.io
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */


package io.swagger.client.model;

import java.util.Objects;
import java.util.Arrays;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import io.swagger.client.model.OuterEnum;
import java.io.IOException;
import android.os.Parcelable;
import android.os.Parcel;

/**
 * EnumTest
 */

public class EnumTest implements Parcelable {
  /**
   * Gets or Sets enumString
   */
  @JsonAdapter(EnumStringEnum.Adapter.class)
  public enum EnumStringEnum {
    UPPER("UPPER"),
    
    LOWER("lower"),
    
    EMPTY("");

    private String value;

    EnumStringEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static EnumStringEnum fromValue(String text) {
      for (EnumStringEnum b : EnumStringEnum.values()) {
        if (String.valueOf(b.value).equals(text)) {
          return b;
        }
      }
      return null;
    }

    public static class Adapter extends TypeAdapter<EnumStringEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final EnumStringEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public EnumStringEnum read(final JsonReader jsonReader) throws IOException {
        String value = jsonReader.nextString();
        return EnumStringEnum.fromValue(String.valueOf(value));
      }
    }
  }

  @SerializedName("enum_string")
  private EnumStringEnum enumString = null;

  /**
   * Gets or Sets enumStringRequired
   */
  @JsonAdapter(EnumStringRequiredEnum.Adapter.class)
  public enum EnumStringRequiredEnum {
    UPPER("UPPER"),
    
    LOWER("lower"),
    
    EMPTY("");

    private String value;

    EnumStringRequiredEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static EnumStringRequiredEnum fromValue(String text) {
      for (EnumStringRequiredEnum b : EnumStringRequiredEnum.values()) {
        if (String.valueOf(b.value).equals(text)) {
          return b;
        }
      }
      return null;
    }

    public static class Adapter extends TypeAdapter<EnumStringRequiredEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final EnumStringRequiredEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public EnumStringRequiredEnum read(final JsonReader jsonReader) throws IOException {
        String value = jsonReader.nextString();
        return EnumStringRequiredEnum.fromValue(String.valueOf(value));
      }
    }
  }

  @SerializedName("enum_string_required")
  private EnumStringRequiredEnum enumStringRequired = null;

  /**
   * Gets or Sets enumInteger
   */
  @JsonAdapter(EnumIntegerEnum.Adapter.class)
  public enum EnumIntegerEnum {
    NUMBER_1(1),
    
    NUMBER_MINUS_1(-1);

    private Integer value;

    EnumIntegerEnum(Integer value) {
      this.value = value;
    }

    public Integer getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static EnumIntegerEnum fromValue(String text) {
      for (EnumIntegerEnum b : EnumIntegerEnum.values()) {
        if (String.valueOf(b.value).equals(text)) {
          return b;
        }
      }
      return null;
    }

    public static class Adapter extends TypeAdapter<EnumIntegerEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final EnumIntegerEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public EnumIntegerEnum read(final JsonReader jsonReader) throws IOException {
        int value = jsonReader.nextInt();
        return EnumIntegerEnum.fromValue(String.valueOf(value));
      }
    }
  }

  @SerializedName("enum_integer")
  private EnumIntegerEnum enumInteger = null;

  /**
   * Gets or Sets enumNumber
   */
  @JsonAdapter(EnumNumberEnum.Adapter.class)
  public enum EnumNumberEnum {
    NUMBER_1_DOT_1(1.1),
    
    NUMBER_MINUS_1_DOT_2(-1.2);

    private Double value;

    EnumNumberEnum(Double value) {
      this.value = value;
    }

    public Double getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static EnumNumberEnum fromValue(String text) {
      for (EnumNumberEnum b : EnumNumberEnum.values()) {
        if (String.valueOf(b.value).equals(text)) {
          return b;
        }
      }
      return null;
    }

    public static class Adapter extends TypeAdapter<EnumNumberEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final EnumNumberEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public EnumNumberEnum read(final JsonReader jsonReader) throws IOException {
        String value = jsonReader.nextString();
        return EnumNumberEnum.fromValue(String.valueOf(value));
      }
    }
  }

  @SerializedName("enum_number")
  private EnumNumberEnum enumNumber = null;

  @SerializedName("outerEnum")
  private OuterEnum outerEnum = null;

  public EnumTest() {
  }
  public EnumTest enumString(EnumStringEnum enumString) {
    this.enumString = enumString;
    return this;
  }

   /**
   * Get enumString
   * @return enumString
  **/
  @ApiModelProperty(value = "")
  public EnumStringEnum getEnumString() {
    return enumString;
  }

  public void setEnumString(EnumStringEnum enumString) {
    this.enumString = enumString;
  }

  public EnumTest enumStringRequired(EnumStringRequiredEnum enumStringRequired) {
    this.enumStringRequired = enumStringRequired;
    return this;
  }

   /**
   * Get enumStringRequired
   * @return enumStringRequired
  **/
  @ApiModelProperty(required = true, value = "")
  public EnumStringRequiredEnum getEnumStringRequired() {
    return enumStringRequired;
  }

  public void setEnumStringRequired(EnumStringRequiredEnum enumStringRequired) {
    this.enumStringRequired = enumStringRequired;
  }

  public EnumTest enumInteger(EnumIntegerEnum enumInteger) {
    this.enumInteger = enumInteger;
    return this;
  }

   /**
   * Get enumInteger
   * @return enumInteger
  **/
  @ApiModelProperty(value = "")
  public EnumIntegerEnum getEnumInteger() {
    return enumInteger;
  }

  public void setEnumInteger(EnumIntegerEnum enumInteger) {
    this.enumInteger = enumInteger;
  }

  public EnumTest enumNumber(EnumNumberEnum enumNumber) {
    this.enumNumber = enumNumber;
    return this;
  }

   /**
   * Get enumNumber
   * @return enumNumber
  **/
  @ApiModelProperty(value = "")
  public EnumNumberEnum getEnumNumber() {
    return enumNumber;
  }

  public void setEnumNumber(EnumNumberEnum enumNumber) {
    this.enumNumber = enumNumber;
  }

  public EnumTest outerEnum(OuterEnum outerEnum) {
    this.outerEnum = outerEnum;
    return this;
  }

   /**
   * Get outerEnum
   * @return outerEnum
  **/
  @ApiModelProperty(value = "")
  public OuterEnum getOuterEnum() {
    return outerEnum;
  }

  public void setOuterEnum(OuterEnum outerEnum) {
    this.outerEnum = outerEnum;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    EnumTest enumTest = (EnumTest) o;
    return Objects.equals(this.enumString, enumTest.enumString) &&
        Objects.equals(this.enumStringRequired, enumTest.enumStringRequired) &&
        Objects.equals(this.enumInteger, enumTest.enumInteger) &&
        Objects.equals(this.enumNumber, enumTest.enumNumber) &&
        Objects.equals(this.outerEnum, enumTest.outerEnum);
  }

  @Override
  public int hashCode() {
    return Objects.hash(enumString, enumStringRequired, enumInteger, enumNumber, outerEnum);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class EnumTest {\n");
    
    sb.append("    enumString: ").append(toIndentedString(enumString)).append("\n");
    sb.append("    enumStringRequired: ").append(toIndentedString(enumStringRequired)).append("\n");
    sb.append("    enumInteger: ").append(toIndentedString(enumInteger)).append("\n");
    sb.append("    enumNumber: ").append(toIndentedString(enumNumber)).append("\n");
    sb.append("    outerEnum: ").append(toIndentedString(outerEnum)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(java.lang.Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }


  public void writeToParcel(Parcel out, int flags) {
    out.writeValue(enumString);
    out.writeValue(enumStringRequired);
    out.writeValue(enumInteger);
    out.writeValue(enumNumber);
    out.writeValue(outerEnum);
  }

  EnumTest(Parcel in) {
    enumString = (EnumStringEnum)in.readValue(null);
    enumStringRequired = (EnumStringRequiredEnum)in.readValue(null);
    enumInteger = (EnumIntegerEnum)in.readValue(null);
    enumNumber = (EnumNumberEnum)in.readValue(null);
    outerEnum = (OuterEnum)in.readValue(OuterEnum.class.getClassLoader());
  }

  public int describeContents() {
    return 0;
  }

  public static final Parcelable.Creator<EnumTest> CREATOR = new Parcelable.Creator<EnumTest>() {
    public EnumTest createFromParcel(Parcel in) {
      return new EnumTest(in);
    }
    public EnumTest[] newArray(int size) {
      return new EnumTest[size];
    }
  };
}

